import argparse
from train import train, evaluate_on_train
import utils
from predict import test


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Training and evaluation script')

    # Add arguments
    parser.add_argument('--train', action='store_true', help='Run training')
    parser.add_argument('--evaluate', action='store_true', help='Run evaluation')

    # Parse arguments
    args = parser.parse_args()

    # Execute based on arguments
    if args.train:
        print("Starting training...")
        train()
    elif args.evaluate:
        print("Starting evaluation...")
        evaluate_on_train()
    else:
        print("Please specify --train or --evaluate")


if __name__ == "__main__":
    main()
