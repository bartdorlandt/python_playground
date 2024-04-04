import argparse
import logging


def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""Title.

        Some description...
        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--no-upload", action="store_true", help="Do not upload any results", default=False)
    parser.add_argument(
        "-L",
        "--loglevel",
        type=str,
        help="Set the desired loglevel",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        required=False,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    do_upload = not args.no_upload
    logging.getLogger().setLevel(args.loglevel)
    logging.info("Do something...")
    logging.error("That is not good...")
