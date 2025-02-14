#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from pydantic import BaseModel, Field

MIN_MESSAGE_LENGTH = int(os.getenv("ARGILLA_MIN_MESSAGE_LENGTH", 1))
MAX_MESSAGE_LENGTH = int(os.getenv("ARGILLA_MAX_MESSAGE_LENGTH", 20000))

MIN_ROLE_LENGTH = int(os.getenv("ARGILLA_MIN_ROLE_LENGTH", 1))
MAX_ROLE_LENGTH = int(os.getenv("ARGILLA_MAX_ROLE_LENGTH", 20))


class ChatFieldValue(BaseModel):
    role: str = Field(..., min_length=MIN_ROLE_LENGTH, max_length=MAX_ROLE_LENGTH)
    content: str = Field(..., min_length=MIN_MESSAGE_LENGTH, max_length=MAX_MESSAGE_LENGTH)
