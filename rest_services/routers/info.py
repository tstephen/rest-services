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
"""
info.py
"""
from __future__ import annotations

import logging
import sys
from typing import List

from fastapi import APIRouter

from rest_services.constants import Tool
from rest_services.models.models import AppMetadata

logger = logging.getLogger(__name__)
info_router = APIRouter(tags=["info"])


@info_router.get(
    path="/info",
    description="Get information about the application",
    summary="Information about the application",
    response_model=AppMetadata,
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "name": "ExampleApp",
                        "vendor": "ExampleVendor",
                        "version": "1.0.0",
                        "python_version": "3.9.1"
                    }
                }
            }
        }
    }
)
def get_info() -> AppMetadata:
    meta = AppMetadata()
    meta.name = Tool.NAME
    meta.vendor = Tool.VENDOR
    meta.version = Tool.VERSION
    meta.python_version = ".".join(map(str, sys.version_info[:3]))
    return meta
