cmake_minimum_required(VERSION 3.14)
project({{package_name}})

find_package(autoware_cmake REQUIRED)
autoware_package()

ament_auto_add_library({{package_name}} SHARED
  src/{{package_name}}.cpp
)
ament_target_dependencies({{package_name}})

rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN "{{package_name}}::{{PackageName}}"
  EXECUTABLE ${PROJECT_NAME}_node
)

ament_auto_package(
  INSTALL_TO_SHARE
  launch
  config
)
