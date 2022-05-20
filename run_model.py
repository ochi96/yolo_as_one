

from argparse import ArgumentParser
from yolo_as_one.models import run_models

from argparse import ArgumentParser
from subprocess import call
from sys import platform

# model_names = ['yolox', 'yolor', 'yolov5']

# def run_models(args):
#     if args.model_name in model_names:
#         if platform == "linux" or platform == "linux2":
#             call(f"/media/bram/PlayField/Projects/Freelancing/Ritesh_YOLO/yolo_as_one/src/inference_scripts/{args.model_name}_inferencing.sh {args.source} {args.save_dir}", shell=True)
#         elif platform == "win32":
#             call(f"{args.model_name}_inferencing.bat {args.source} {args.save_dir}", shell=True)
#         else:
#             print('Operating Sytem unsupported')
#     else:
#         print('model currently unavailable')
#     pass


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("--model_name", type=str,
                        help="specify the model to test")
    parser.add_argument("--source",
                        help="specify the source: image, video or webcam=0",
                        default='image')
    parser.add_argument("--save_dir",type=str, help="results are saved here",
                        default=False)
    parser.add_argument('--view_img', action='store_true', help='show results',
                        default=False)
    args = parser.parse_args()

    run_models(args)
