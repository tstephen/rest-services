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
import logging
import time
from fastapi import FastAPI

from rest_services.constants import Tool
from rest_services.routers.info import info_router
from rest_services.routers.items import item_router


logger = logging.getLogger(__name__)
start_time = time.perf_counter()
app = FastAPI(
    title=f"{Tool.NAME} API",
    version=Tool.VERSION,
)
app.include_router(info_router)
app.include_router(item_router)


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)