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

from datetime import datetime
from optparse import Option
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class Workspace(BaseModel):
    id: UUID
    name: str
    inserted_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class WorkspaceCreate(BaseModel):
    id: Optional[UUID] = None
    name: str = Field(min_length=1)


class Workspaces(BaseModel):
    items: List[Workspace]


class WorkspaceUserCreate(BaseModel):
    user_id: UUID
