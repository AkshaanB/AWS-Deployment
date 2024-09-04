import argparse
from typing import Union


def create_tar(model_dir: str) -> str:
    """Create the tar file/s

    Args:
        model_dir (str): The model directory (default=models/data)

    Returns:
        str: The response of tar file creation
    """
    

def delete_endpoint(region: str) -> str:
    """Method to delete an endpoint

    Args:
        region (str): AWS region

    Returns:
        str: The response of endpoint deletion
    """


def create_endpoint(region: str, instance: str, model: str) -> Union[str, bool]:
    """Method to create the endpoint

    Args:
        region (str): AWS region
        instance (str): The instance of the endpoint
        model (str): Model/s that need to be deployed

    Returns:
        Union[str, bool]: The response message of endpoint creation, True if successfully created False if not
    """

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Deploying models to AWS Sagemaker endpoint")
    
    parser.add_argument('--delete', action='store_true', default=False, help='Delete the endpoint')
    parser.add_argument('--create', action='store_true', default=False, help='Create the endpoint')
    parser.add_argument('--region', default='us-east-1', type=str, help='Region that the model should be deployed')
    parser.add_argument('--instance', default='m4.xlarge', type=str, help='The instance that the model is deployed')
    parser.add_argument('--model', type=str, nargs='+', help='Model/s to be deployed')

    args = parser.parse_args()

    if args.delete:
        response = delete_endpoint(args.region)
        print(response)

    if args.create:
        response = create_endpoint(args.region, args.instance, args.model)
        print(response)
