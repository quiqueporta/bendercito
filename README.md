# bendercito
Change your Slack status from command line.

## Install

To install **bendercito**, just run:

```sh
$ sudo pip install bendercito
```

## Configure

First create a config file with your favorite status.

Example config.json:

```javascript
{
  "clean":
  {
    "emoji": "",
    "message": ""
  },
  "pomodoro":
  {
    "emoji": ":tomato:",
    "message": "Pomodoro don't disturb"
  },
  "pairing":
  {
    "emoji": ":beers:",
    "message": "Pairing"
  },
  "open":
  {
    "emoji": ":two_hearts:",
    "message": "Open for Pairing"
  },
  "dinning":
  {
    "emoji": ":fork_and_knife:",
    "message": "Dinning"
  },
  "doctor":
  {
    "emoji": ":syringe:",
    "message": "Doctor visit"
  }
}
```

Then you need to create two environment variables.

```sh
BENDERCITO_FILE="path_to_your_config_file"
BENDERCITO_SLACK_TOKEN="your_slack_token"
```

## Usage

```sh
$ bendercito pairing
```

```sh
$ bendercito --list
```
