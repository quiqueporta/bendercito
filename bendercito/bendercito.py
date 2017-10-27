import argparse
import json
import os
import sys

from slackclient import SlackClient


def main():
    arguments = _parse_arguments()
    available_status = _load_available_status()

    if arguments.list or not arguments.status:
        print("Available status: {}".format(", ".join(sorted(available_status.keys()))))
        return

    _change_status(available_status, arguments.status)

def _parse_arguments():
    parser = argparse.ArgumentParser(description='Bendercito helps you to change your Slack status.')

    parser.add_argument("status", nargs='?', type=str)
    parser.add_argument("-l", "--list",
                        action="store_true",
                        default=False,
                        help="print list of possible status")

    return parser.parse_args()

def _load_available_status():
    with open(_get_env_setting('BENDERCITO_FILE')) as config_file:
        data = json.load(config_file)
        return data

def _change_status(available_status, status):
    try:
        selected_status = available_status[status]
        slack_client = SlackClient(_get_env_setting('BENDERCITO_SLACK_TOKEN'))
        slack_client.api_call(
                "users.profile.set",
                profile={
                    'status_text': selected_status['message'],
                    'status_emoji': selected_status['emoji']
                }
        )
        print("Status changed!")
    except KeyError:
        print("Wait, what? Got a potato in your mouth or something?")
        print("Use --list to show available status")

def _get_env_setting(setting):
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the {} env variable".format(setting)
        raise Exception(error_msg)

if __name__ == "__main__":
    main()
