# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from pydantic import BaseModel, Field
from typing import Union


class AppMetadata(BaseModel):
    name: str = Field(None, description="application name")
    vendor: str = Field(None, description="application vendor")
    version: str = Field(None, description="application version")
    python_version: str = Field(
        None, alias="python-version", description="python version"
    )


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
