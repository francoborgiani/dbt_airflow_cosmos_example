"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
import os
from include.constants import profiles_jaffle_shop_path


airflow_db = ProfileConfig(
    profile_name="jaffle_shop",
    target_name=os.environ["DBT_TARGET"],
    profiles_yml_filepath=profiles_jaffle_shop_path
)
