cmake_minimum_required(VERSION 3.10.0)
project(school)

find_package(OpenCV REQUIRED)

include_directories(include )

set (HERDERS
	include/utils.hpp
	include/db.hpp
)

set (SOURCES
	src/utils.cpp
	src/db.cpp
)
#include_directories(${OpenCV_INCLUDE_DIRS})
#link_directories (${OpenCV_LIBRARY_DIRS})
#add_library(utils include/utils.hpp src/utils.cpp)

#add_executable(imshow src/imshow.cpp)

add_executable(cm src/cp.cpp ${HERDERS} ${SOURCES})
add_executable(db src/main.cpp ${HERDERS} ${SOURCES})
#target_link_libraries (imshow ${OpenCV_LIBRARIES})

install(DIRECTORY 
	cm
	db
	DESTINATION ~/
	)
