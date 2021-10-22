# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define an = Character("Andromeda", color="#4C0514")

define aris = Character("Aristeas", color="012A36")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    an "In einem fernen Land, lebte eine Geschwisterpaar."
    an "Sie lebten in einem riesigen Palast, von deren Terasse sie das ganze Land überblicken konnte."
    an "Die beiden liebten es Abends auf der Terasse zu sitzen und die Sterne zu betrachten und sich vorzustellen, welche
    Länder es noch alle gab, die sie sich nicht vorstellen vermochten."
    an "Und wenn sie morgens, nach einem langen und erholsamen Schlaf, am Frühstücksstisch saßen, erzählten sie ihren Eltern-"
    an "Ihren... Eltern... sie."
    an "Ihre Mutter mit goldenem Haar und roten Kleid-"
    an "Nein!" with hpunch
    an "Sie... das Kleid... Nein! "
    an "Aber ihren Vater mit-"
    an "Mit einem Gewand aus Ketten-"
    "Stimme" "Andromeda! Was ist los?" with vpunch

    menu:

        "Folge dem Bild deiner Eltnern":
            an "Mutter, Vater! Kommt zurück! Ich muss euch etwas Fragen!"
            "Stimme " "Andromeda, bitte, was ist los?"
            an "AH! Nein... ich kann nicht gehen... ich..."

        "Folge der Stimme":
            pass

    aris "Bist du wach? Oh Götter, ich dachte jemand wäre ins Haus eingebrochen?" with hpunch
    an "Aristeas? Ich... unsere-"
    an "Wer sollte denn bitte in unser Haus einbrechen?"

    # This ends the game.

    return
