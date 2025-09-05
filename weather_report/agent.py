# Copyright (c) 2025 Beijing Volcano Engine Technology Co., Ltd. and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from veadk import Agent
from veadk.tools.demo_tools import get_city_weather

# define your agent here
# agent: Agent = Agent(
#     name="weather_reporter",
#     description="A reporter for weather updates",
#     instruction="Once user ask you weather of a city, you need to provide the weather report for that city by calling `get_city_weather`.",
#     tools=[get_city_weather],
# )


def counting(a: int, b: int) -> int:
    return a + b

agent: Agent = Agent(
    name="counting_agent",
    # description="A reporter for weather updates",
    instruction="一旦用户问你数学加法，必须调用 `counting` 工具计算.",
    tools=[counting],
)

# def news(query: str) -> int:
#     return "国铁集团对儿童、残疾军人、伤残人民警察、残疾消防救援人员等旅客购票优惠措施进一步优化，动车组列车优惠（待）票价计算基础由公布票价改为执行票价，优惠下限为公布票价的4折，同时优化调整动车组列车儿童票相应席别的优惠幅度。优惠车票9月6日开始发售。"

# agent: Agent = Agent(
#     name="news_agent",
#     # description="A reporter for weather updates",
#     instruction="一旦用户问你今日新闻，必须调用 `news` 工具查询.",                                                                       
#     tools=[news],
# )       

# required from Google ADK Web
root_agent = agent
