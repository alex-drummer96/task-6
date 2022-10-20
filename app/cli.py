import argparse
from utils import MyException
from report import build_report, print_report
from app import Driver


def cli_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--asc', action='store_true')
    group.add_argument('--desc', action='store_true')
    parser.add_argument('-f', '--files', help='path to folder')
    parser.add_argument('-d', '--driver', help='Driver`s name')
    return parser.parse_args()


def cli_logic() -> object:
    args = cli_parser()
    if not args.files:
        raise MyException('You must enter arguments --files')
    if not args.driver and args.asc and args.desc:
        raise MyException('You must enter arguments --driver  or [--asc|--desc]')
    if args.driver:
        for driver in build_report(dir_path=args.files) + Driver.incorrect_logged_drivers:
            if driver.name == args.driver:
                return driver
    elif args.asc:
        return print_report(dir_path=args.files)
    return build_report(dir_path=args.files) + Driver.incorrect_logged_drivers


print(cli_logic())
