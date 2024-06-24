// Copyright {{year}} TIER IV, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef {{PACKAGE_NAME}}__{{PACKAGE_NAME}}_HPP_
#define {{PACKAGE_NAME}}__{{PACKAGE_NAME}}_HPP_

#include <rclcpp/rclcpp.hpp>

namespace {{package_name}}
{

class {{PackageName}} : public rclcpp::Node
{
public:
  explicit {{PackageName}}(const rclcpp::NodeOptions & node_options);
  ~{{PackageName}}() = default;

private:
};
}  // namespace {{package_name}}

#endif  // {{PACKAGE_NAME}}__{{PACKAGE_NAME}}_HPP_