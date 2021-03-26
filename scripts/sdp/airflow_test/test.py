import argparse


def main(state, env):
    print(state, env)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Wrapper script for integrating config per state'
    )

    parser.add_argument(
        '--state',
        type=str,
        help='State which is about to be deployed',
        required=True,
    )

    parser.add_argument(
        '--env',
        type=str,
        help='environment (dev, nonprod, cert, prod) which config should be applied',
        required=True,
    )

    args = parser.parse_args()
    main(args.env, args.state)
