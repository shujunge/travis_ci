project(tensor_mat)

#file(GLOB zflib my_lib.cpp)
#add_library(zflib SHARED ${zflib})

include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable(out main.cpp  my_lib.cpp my_lib.h)
target_link_libraries(out ${TORCH_LIBRARIES} ${OpenCV_LIBS} ${EIGEN3_LIBS} )
set_property(TARGET out PROPERTY CXX_STANDARD 11)

