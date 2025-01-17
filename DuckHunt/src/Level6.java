import javafx.application.Platform;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.Pane;

public class Level6 extends Level{
    int ammo = 9;

    Duck blackDuck = new Duck("black", 0, 40);
    Duck blueDuck = new Duck("blue", 0, 80);
    Duck redDuck = new Duck("red", 220, 135);

    Duck[] ducks = {blackDuck, blueDuck, redDuck};

    public Level6(ImageView chosenForegImgView, ImageView chosenBgImgView, ImageView chosenCrosImgView) {
        super(chosenForegImgView, chosenBgImgView, chosenCrosImgView);
    }

    protected void play(){
        blackDuck.flyHorizontally(true);
        blueDuck.flyDiagonally(true, false);
        redDuck.flyDiagonally(false, false);

        root = new Pane(chosenBgImgView, blackDuck.getCurrentDuckImgView(), blueDuck.getCurrentDuckImgView(), redDuck.getCurrentDuckImgView(), chosenForegImgView,
                chosenCrosImgView, levelText, ammoText);
        root.setCursor(Cursor.NONE);
        levelText.setText("Level 6/6");
        ammoText.setText("Ammo left :" + ammo);

        levelScene = new Scene(root, DuckHunt.width, DuckHunt.height);
        crossMovement();

        levelScene.setOnMouseClicked(event -> {
            if(ammo > 0){
                if(killedDucks != 3){
                    fireShotIfPossible(ammo--);
                    ammoText.setText("Ammo left :" + ammo);
                }

                for(Duck duck : ducks){
                    if(duck.isAlive()){
                        if(duck.getCurrentDuckImgView().getBoundsInParent().intersects(chosenCrosImgView.getBoundsInParent())){
                            duck.killDuck();
                            killedDucks++;
                        }
                    }
                }
            }

            // read when level is successfully completed
            if(killedDucks == 3 && !instructionText.getText().equals("Press ENTER to play again\n\tPress ESC to exit")){
                gameCompletedMP.play();
                levelPassedText.setText("You have completed the game!");
                levelPassedText.setLayoutX(27*DuckHunt.scale);
                instructionText.setText("Press ENTER to play again\n\tPress ESC to exit");
                instructionText.setLayoutX(39*DuckHunt.scale);
                root.getChildren().addAll(levelPassedText, instructionText);
                levelScene.setOnKeyPressed(event1 -> {
                    if(event1.getCode() == KeyCode.ENTER){
                        gameCompletedMP.stop();
                        playTheChosenLevel(1);
                    }else if(event1.getCode() == KeyCode.ESCAPE){
                        gameCompletedMP.stop();
                        WelcomeScreen welcomeScreen = new WelcomeScreen("assets/welcome/1.png", "assets/effects/Title.mp3");
                        welcomeScreen.manageWelcomeScreen();
                    }
                });

            }




            // read when the user fails to complete
            if(ammo == 0 && killedDucks != 3 && !instructionText.getText().equals("Press ENTER to play again\n\tPress ESC to exit")){
                gameOverMP.play();
                instructionText.setText("Press ENTER to play again\n\tPress ESC to exit");
                instructionText.setLayoutX(40*DuckHunt.scale);
                root.getChildren().addAll(gameOverText, instructionText);
                levelScene.setOnKeyPressed(event1 -> {
                    if(event1.getCode() == KeyCode.ENTER){
                        gameOverMP.stop();
                        playTheChosenLevel(1);
                    } else if (event1.getCode() == KeyCode.ESCAPE) {
                        gameOverMP.stop();
                        WelcomeScreen welcomeScreen = new WelcomeScreen("assets/welcome/1.png", "assets/effects/Title.mp3");
                        welcomeScreen.manageWelcomeScreen();
                    }
                });
            }
        });

        DuckHunt.stage.setScene(levelScene);
    }
}
