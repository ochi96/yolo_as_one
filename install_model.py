from yolo_as_one.models import install_models
from argparse import ArgumentParser



if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("--model_name", type=str,
                        help="specify the model to install")
    args = parser.parse_args()

    install_models(args.model_name)