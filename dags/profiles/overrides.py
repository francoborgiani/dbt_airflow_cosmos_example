from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

from include.constants import jaffle_shop_path, venv_execution_config, profiles_jaffle_shop_path
import os

dbt_profile_overrides = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(jaffle_shop_path),
    profile_config=ProfileConfig(
        # these map to dbt/jaffle_shop/profiles.yml
        profile_name="jaffle_shop",
        target_name=os.environ["DBT_TARGET"],
        profiles_yml_filepath=profiles_jaffle_shop_path,
    ),
    execution_config=venv_execution_config,
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_profile_overrides",
    tags=["profiles"],
)
