import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore
from fantasy_cricket_ui import Ui_MainWindow
from scoring_rules import ScoringRules

class FantasyCricketApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(FantasyCricketApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize variables
        self.total_points = 1000
        self.used_points = 0
        self.available_points = 1000
        self.selected_players = []
        self.team_name = ""
        
        # Connect signals and slots
        self.ui.radioButtonBAT.clicked.connect(lambda: self.populate_players("BAT"))
        self.ui.radioButtonBOW.clicked.connect(lambda: self.populate_players("BWL"))
        self.ui.radioButtonAR.clicked.connect(lambda: self.populate_players("AR"))
        self.ui.radioButtonWK.clicked.connect(lambda: self.populate_players("WK"))
        
        self.ui.listWidgetPlayers.itemDoubleClicked.connect(self.add_player)
        self.ui.listWidgetSelected.itemDoubleClicked.connect(self.remove_player)
        
        # Menu actions
        self.ui.actionNew_Team.triggered.connect(self.new_team)
        self.ui.actionOpen_Team.triggered.connect(self.open_team)
        self.ui.actionSave_Team.triggered.connect(self.save_team)
        self.ui.actionEvaluate_Team.triggered.connect(self.evaluate_team)
        
        # Initially populate with BAT players
        try:
            self.populate_players("BAT")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Initialization Error", f"Failed to initialize player list: {str(e)}")
        
    def connect_database(self):
        """Establish connection to the database."""
        try:
            conn = sqlite3.connect('fantasy_cricket.db')
            # Check if tables exist
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS match (
                Player TEXT PRIMARY KEY,
                Scored INTEGER,
                Faced INTEGER,
                Fours INTEGER,
                Sixes INTEGER,
                Bowled INTEGER,
                Maiden INTEGER,
                Given INTEGER,
                Wkts INTEGER,
                Catches INTEGER,
                Stumping INTEGER,
                RO INTEGER
            )""")
            
            cursor.execute("""CREATE TABLE IF NOT EXISTS stats (
                player TEXT PRIMARY KEY,
                matches INTEGER,
                runs INTEGER,
                "100s" INTEGER,
                "50s" INTEGER,
                value INTEGER,
                ctg TEXT
            )""")
            
            cursor.execute("""CREATE TABLE IF NOT EXISTS teams (
                name TEXT PRIMARY KEY,
                players TEXT,
                value INTEGER
            )""")
            
            conn.commit()
            return conn
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to connect to database: {str(e)}")
            return None
    
    def populate_players(self, category):
        """Populate the players list based on category."""
        conn = self.connect_database()
        if not conn:
            return
            
        cursor = conn.cursor()
        
        # Clear the list first
        self.ui.listWidgetPlayers.clear()
        
        # Get players of the selected category
        try:
            cursor.execute("SELECT player, value, ctg FROM stats WHERE ctg=?", (category,))
            players = cursor.fetchall()
            
            # Add players to the list
            for player in players:
                item_text = f"{player[0]} - {player[1]} points"
                item = QtWidgets.QListWidgetItem(item_text)
                item.setData(QtCore.Qt.UserRole, player)  # Store player data
                self.ui.listWidgetPlayers.addItem(item)
                
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to fetch players: {str(e)}")
        finally:
            conn.close()
    
    def add_player(self, item):
        """Add a player to the selected players list."""
        try:
            # Check if team name is set
            if not self.team_name:
                QtWidgets.QMessageBox.warning(self, "No Team", "Please create a new team first!")
                return
                
            # Check if 11 players are already selected
            if len(self.selected_players) >= 11:
                QtWidgets.QMessageBox.warning(self, "Team Full", "You can only select 11 players!")
                return
                
            # Get player data
            # Get player data
            player_data = item.data(QtCore.Qt.UserRole)
            if not player_data or len(player_data) < 3:
                QtWidgets.QMessageBox.warning(self, "Invalid Player Data", "Player data is incomplete or invalid!")
                return
                
            player_name = player_data[0]
            player_value = player_data[1]
            player_category = player_data[2]  # Category is now included in player_data
            
            # Validate player data
            if not player_name or not isinstance(player_value, int) or not player_category:
                QtWidgets.QMessageBox.warning(self, "Invalid Player Data", "Player data is invalid!")
                return
            
            # Check if player is already selected
            if player_name in [p[0] for p in self.selected_players]:
                QtWidgets.QMessageBox.warning(self, "Player Already Selected", f"{player_name} is already in your team!")
                return
                
            # Check if we have enough points
            if self.available_points < player_value:
                QtWidgets.QMessageBox.warning(self, "Not Enough Points", "You don't have enough points to buy this player!")
                return
                
            # Check category constraints (2-5 batsmen, 2-5 bowlers, 1-3 all-rounders, 1-1 wicketkeeper)
            bat_count = sum(1 for p in self.selected_players if p[2] == "BAT")
            bow_count = sum(1 for p in self.selected_players if p[2] == "BWL")
            ar_count = sum(1 for p in self.selected_players if p[2] == "AR")
            wk_count = sum(1 for p in self.selected_players if p[2] == "WK")
            
            if player_category == "BAT" and bat_count >= 5:
                QtWidgets.QMessageBox.warning(self, "Category Limit", "You can select maximum 5 batsmen!")
                return
            elif player_category == "BWL" and bow_count >= 5:
                QtWidgets.QMessageBox.warning(self, "Category Limit", "You can select maximum 5 bowlers!")
                return
            elif player_category == "AR" and ar_count >= 3:
                QtWidgets.QMessageBox.warning(self, "Category Limit", "You can select maximum 3 all-rounders!")
                return
            elif player_category == "WK" and wk_count >= 1:
                QtWidgets.QMessageBox.warning(self, "Category Limit", "You can select maximum 1 wicketkeeper!")
                return
                
            # Add player to selected list
            # Store as (player_name, player_value, player_category)
            self.selected_players.append((player_name, player_value, player_category))
            
            # Update points
            self.used_points += player_value
            self.available_points -= player_value
            self.update_points_display()
            
            # Update selected players list
            self.update_selected_players_list()
            
            # Remove from available players list
            self.ui.listWidgetPlayers.takeItem(self.ui.listWidgetPlayers.row(item))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error Adding Player", f"Failed to add player: {str(e)}")
    
    def remove_player(self, item):
        """Remove a player from the selected players list."""
        try:
            # Get player name from the item
            player_text = item.text()
            if not player_text:
                QtWidgets.QMessageBox.warning(self, "Invalid Player", "Player information is invalid!")
                return
                
            player_parts = player_text.split(" - ")
            if not player_parts or len(player_parts) < 1:
                QtWidgets.QMessageBox.warning(self, "Invalid Player", "Player information is invalid!")
                return
                
            player_name = player_parts[0]
            
            # Find and remove player from selected players
            player_found = False
            for i, player in enumerate(self.selected_players):
                if player[0] == player_name:
                    removed_player = self.selected_players.pop(i)
                    player_value = removed_player[1]
                    player_found = True
                    
                    # Update points
                    self.used_points -= player_value
                    self.available_points += player_value
                    self.update_points_display()
                    
                    # Update selected players list
                    self.update_selected_players_list()
                    
                    # Add back to available players list based on current category
                    current_category = ""
                    if self.ui.radioButtonBAT.isChecked():
                        current_category = "BAT"
                    elif self.ui.radioButtonBOW.isChecked():
                        current_category = "BWL"
                    elif self.ui.radioButtonAR.isChecked():
                        current_category = "AR"
                    elif self.ui.radioButtonWK.isChecked():
                        current_category = "WK"
                    
                    # Check if the removed player belongs to the current category
                    conn = self.connect_database()
                    if conn:
                        cursor = conn.cursor()
                        try:
                            cursor.execute("SELECT player, value, ctg FROM stats WHERE player=?", (player_name,))
                            player_data = cursor.fetchone()
                            if player_data and player_data[2] == current_category:
                                # Only add back if the player belongs to the current category
                                item_text = f"{player_data[0]} - {player_data[1]} points"
                                list_item = QtWidgets.QListWidgetItem(item_text)
                                list_item.setData(QtCore.Qt.UserRole, player_data)
                                self.ui.listWidgetPlayers.addItem(list_item)
                        except sqlite3.Error as e:
                            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to fetch player: {str(e)}")
                        finally:
                            conn.close()
                    break
                    
            if not player_found:
                QtWidgets.QMessageBox.warning(self, "Player Not Found", "Could not find the selected player!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error Removing Player", f"Failed to remove player: {str(e)}")
    
    def update_selected_players_list(self):
        """Update the selected players list display."""
        try:
            self.ui.listWidgetSelected.clear()
            for player in self.selected_players:
                # Validate player data
                if not player or len(player) < 3:
                    continue
                item_text = f"{player[0]} - {player[1]} points ({player[2]})"
                self.ui.listWidgetSelected.addItem(item_text)
                
            # Update the group box title
            self.ui.groupBox_2.setTitle(f"Selected Players ({len(self.selected_players)}/11)")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Display Error", f"Failed to update player list display: {str(e)}")
    
    def update_points_display(self):
        """Update the points display labels."""
        try:
            self.ui.labelPointsAvailable.setText(f"Points Available: {self.available_points}")
            self.ui.labelPointsUsed.setText(f"Points Used: {self.used_points}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Display Error", f"Failed to update points display: {str(e)}")
    
    def new_team(self):
        """Create a new team."""
        try:
            team_name, ok = QtWidgets.QInputDialog.getText(self, "New Team", "Enter team name:")
            if ok and team_name:
                self.team_name = team_name
                self.selected_players = []
                self.used_points = 0
                self.available_points = 1000
                self.update_points_display()
                self.update_selected_players_list()
                self.statusBar().showMessage(f"New team '{team_name}' created")
            elif ok:
                QtWidgets.QMessageBox.warning(self, "Invalid Name", "Please enter a valid team name!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Team Creation Error", f"Failed to create new team: {str(e)}")
    
    def open_team(self):
        """Open an existing team."""
        try:
            conn = self.connect_database()
            if not conn:
                return
                
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT name FROM teams")
                teams = cursor.fetchall()
                
                if not teams:
                    QtWidgets.QMessageBox.information(self, "No Teams", "No saved teams found!")
                    return
                    
                team_names = [team[0] for team in teams]
                team_name, ok = QtWidgets.QInputDialog.getItem(self, "Open Team", "Select team:", team_names, 0, False)
                
                if ok and team_name:
                    # Load team data
                    cursor.execute("SELECT players, value FROM teams WHERE name=?", (team_name,))
                    team_data = cursor.fetchone()
                    
                    if team_data:
                        self.team_name = team_name
                        players_str = team_data[0]
                        team_value = team_data[1]
                        
                        # Parse players
                        self.selected_players = []
                        if players_str:
                            player_names = players_str.split(",")
                            for player_name in player_names:
                                player_name = player_name.strip()
                                if player_name:
                                    # Get player details
                                    cursor.execute("SELECT player, value, ctg FROM stats WHERE player=?", (player_name,))
                                    player_data = cursor.fetchone()
                                    if player_data:
                                        # Store as (player_name, player_value, player_category)
                                        self.selected_players.append(player_data)
                        
                        # Update points
                        self.used_points = team_value
                        self.available_points = 1000 - team_value
                        self.update_points_display()
                        self.update_selected_players_list()
                        self.statusBar().showMessage(f"Team '{team_name}' loaded")
                        
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to open team: {str(e)}")
            finally:
                conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Team Loading Error", f"Failed to load team: {str(e)}")
    
    def save_team(self):
        """Save the current team."""
        try:
            if not self.team_name:
                QtWidgets.QMessageBox.warning(self, "No Team", "Please create a new team first!")
                return
                
            if len(self.selected_players) != 11:
                QtWidgets.QMessageBox.warning(self, "Incomplete Team", 
                                            f"Please select 11 players (currently {len(self.selected_players)})!")
                return
                
            conn = self.connect_database()
            if not conn:
                return
                
            cursor = conn.cursor()
            try:
                # Create comma-separated player names
                player_names = ",".join([player[0] for player in self.selected_players])
                
                # Save or update team
                cursor.execute("INSERT OR REPLACE INTO teams (name, players, value) VALUES (?, ?, ?)",
                              (self.team_name, player_names, self.used_points))
                conn.commit()
                self.statusBar().showMessage(f"Team '{self.team_name}' saved successfully")
                QtWidgets.QMessageBox.information(self, "Success", f"Team '{self.team_name}' saved successfully!")
                
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to save team: {str(e)}")
            finally:
                conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Team Saving Error", f"Failed to save team: {str(e)}")
    
    def evaluate_team(self):
        """Evaluate the team score."""
        try:
            if not self.team_name:
                QtWidgets.QMessageBox.warning(self, "No Team", "Please create and save a team first!")
                return
                
            if len(self.selected_players) != 11:
                QtWidgets.QMessageBox.warning(self, "Incomplete Team", 
                                            f"Please select 11 players (currently {len(self.selected_players)})!")
                return
                
            # Show dialog to select match
            conn = self.connect_database()
            if not conn:
                return
                
            cursor = conn.cursor()
            try:
                # For simplicity, we'll just calculate score based on the data we have
                total_score = 0
                
                for player in self.selected_players:
                    player_name = player[0]
                    
                    # Get player match data
                    cursor.execute("SELECT * FROM match WHERE Player=?", (player_name,))
                    match_data = cursor.fetchone()
                    
                    if match_data:
                        # Calculate player score using the scoring rules module
                        player_score = ScoringRules.calculate_player_score(match_data)
                        total_score += player_score
                
                # Show the result
                msg = f"Team: {self.team_name}\nTotal Score: {total_score}"
                QtWidgets.QMessageBox.information(self, "Team Evaluation", msg)
                
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to evaluate team: {str(e)}")
            finally:
                conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Team Evaluation Error", f"Failed to evaluate team: {str(e)}")

def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = FantasyCricketApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()