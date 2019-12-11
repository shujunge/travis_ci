cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(tensor_mat)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

# direct binary outputs
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)


option(BUILD_TESTS   "Build tests" ON)
option(BUILD_DOCS    "Create build rules for Documentation" ON)

project("multiloc" VERSION 0.5.0)


include_directories( "/usr/local/include/eigen3" )
set(Torch_DIR /libtorch/share/cmake/Torch)

find_package(Torch REQUIRED)
find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)


add_subdirectory(srcs)

if(BUILD_TESTS)
    enable_testing()
    find_package(GTest REQUIRED)
    add_subdirectory(tests)
endif()

#if(BUILD_DOCS)
#    find_package(PythonInterp 3 REQUIRED)
#    find_package(Doxygen REQUIRED)
#    if(PYTHONINTERP_FOUND)
#        find_package(Sphinx REQUIRED)
#    endif()
    #add_subdirectory(docs)
#endif()

IF(BUILD_DOCS)
    set(CMAKE_DOCS_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/docs)
    find_package(Doxygen REQUIRED)
    IF(NOT DOXYGEN_FOUND)
        MESSAGE(FATAL_ERROR "Doxygen is needed to build the documentation.")
    ENDIF()
 
    SET(doxyfile_in ${CMAKE_CURRENT_SOURCE_DIR}/doxygen/Doxyfile.in)
    SET(doxyfile ${CMAKE_CURRENT_BINARY_DIR}/doxygen/Doxyfile)
    SET(srcsfile ${CMAKE_CURRENT_BINARY_DIR}/srcs)
    CONFIGURE_FILE(${doxyfile_in} ${doxyfile} @ONLY)
 
    ADD_CUSTOM_TARGET(doc
        COMMAND ${DOXYGEN_EXECUTABLE} ${doxyfile}
        WORKING_DIRECTORY ${CMAKE_DOCS_OUTPUT_DIRECTORY}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM)
 
    #INSTALL(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/html DESTINATION share/doc)
ENDIF()




#include_directories( ${OpenCV_INCLUDE_DIRS} )
#add_executable(out main.cpp my_lib.cpp my_lib.h)
#target_link_libraries(out ${TORCH_LIBRARIES} ${OpenCV_LIBS} ${EIGEN3_LIBS})
#set_property(TARGET out PROPERTY CXX_STANDARD 11)

message(STATUS "")
message(STATUS "Configurations for ${PROJECT_NAME} (${PROJECT_VERSION})")
message(STATUS "=================================================================")
message(STATUS "  Compilers and options:")
message(STATUS "    C compiler:                ${CMAKE_C_COMPILER} (${CMAKE_C_COMPILER_VERSION})")
message(STATUS "    C flags (Release):         ${CMAKE_C_FLAGS} ${CMAKE_C_FLAGS_RELEASE}")
message(STATUS "    C flags (Debug):           ${CMAKE_C_FLAGS} ${CMAKE_C_FLAGS_DEBUG}")
message(STATUS "    C++ compiler:              ${CMAKE_CXX_COMPILER} (${CMAKE_CXX_COMPILER_VERSION})")
message(STATUS "    C++ flags (Release):       ${CMAKE_CXX_FLAGS} ${CMAKE_CXX_FLAGS_RELEASE}")
message(STATUS "    C++ flags (Debug):         ${CMAKE_CXX_FLAGS} ${CMAKE_CXX_FLAGS_DEBUG}")
message(STATUS "")
message(STATUS "  Libraries:")
message(STATUS "    Eigen3                     ${EIGEN3_VERSION}")
message(STATUS "    libTorch                   ${Torch_VERSION}")
message(STATUS "    OpenCV                     ${OpenCV_VERSION}")
if(BUILD_TESTS)
    message(STATUS "    Google Test                ${GTEST_FOUND}")
endif()

if(BUILD_DOCS)
    message(STATUS "")
    message(STATUS "  Documentation tools:")
    message(STATUS "    Python                     ${PYTHON_EXECUTABLE} (${PYTHON_VERSION_STRING})")
    message(STATUS "    sphinx-build               ${HAVE_SPHINX} (${SPHINX_VERSION})")
    message(STATUS "    Doxygen                    ${DOXYGEN_FOUND} (${DOXYGEN_VERSION})")
    message(STATUS "    XeLaTeX                    ${HAVE_XELATEX} (${XELATEX_VERSION})")
    message(STATUS "    BIBTeX                     ${HAVE_BIBTEX} (${BIBTEX_VERSION})")
endif()
message(STATUS "=================================================================")
message(STATUS "")
