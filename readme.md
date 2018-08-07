# DeathBeam

## Introduction
DeathBeam is a plugin created for [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python).  As such, it requires [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python) to be installed on Source-engine servers.  The plugin shows a beam from the muzzle of the killer's weapon to the point of impact where the bullet hit.

## Installation
To install, simply download the current release from its [release thread](https://forums.sourcepython.com/viewtopic.php?t=1853) and install it into the main directory on your server.  Once you have installed DeathBeam on your server, simply add the following to your autoexec.cfg file:
```
sp plugin load death_beam
```

## Configuration
After having loaded the plugin once, a configuration file will have been created on your server at **../cfg/source-python/death_beam.cfg**  Edit that file to your liking.  The current default configuration file looks like:
```
// Default Value: 10
// Set to the width of the death beam.
   db_beam_width 10


// Default Value: 4
// Set to the number of seconds for death beams to be visible.
   db_beam_time 4


// Default Value: "sprites/laser.vmt"
// Set to which vmt file to use for the deathbeam.
   db_beam_model "sprites/laser.vmt"
```

## Screenshots
The following are screenshots of the menu and messages that accompany this plugin:

**CS:S CT death beam:**

![CS:S CT death beam](https://raw.githubusercontent.com/satoon101/DeathBeam/screenshots/css_ct_death.jpg "CS:GO Menu")

**CS:S CT death beam 2:**

![CS:S CT death beam 2](https://raw.githubusercontent.com/satoon101/DeathBeam/screenshots/css_t_death.jpg "CS:GO Menu")

**CS:S T death beam:**

![CS:S T death beam](https://raw.githubusercontent.com/satoon101/DeathBeam/screenshots/css_ct_bot_death.jpg "CS:GO Menu")

**CS:S T death beam 2:**

![CS:S T death beam 2](https://raw.githubusercontent.com/satoon101/DeathBeam/screenshots/css_t_bot_death.jpg "CS:GO Menu")
