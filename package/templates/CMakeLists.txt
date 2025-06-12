cmake_minimum_required(VERSION 3.14)
project(autoware_{{package_name}})

find_package(autoware_cmake REQUIRED)
autoware_package()

ament_auto_add_library(${PROJECT_NAME} SHARED
  src/{{package_name}}.cpp
)

rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN "autoware::{{package_name}}::{{PackageName}}"
  EXECUTABLE ${PROJECT_NAME}_node
)

ament_auto_package(
  INSTALL_TO_SHARE
  launch
  config
)
