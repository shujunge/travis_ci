cd ../ && mkdir release && cd ./release && cmake .. && make -j8 && make doc && cd .. && rm -rf release 

cd ./docs/latex && make && mv refman.pdf ../ && make clean

cd ../../ && cd ./bin
./out test_image.jpg
./out_test

