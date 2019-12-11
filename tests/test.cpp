#include "../srcs/my_lib.h"

using namespace std;

#include "gtest/gtest.h"

using testing::Test;

/**
 * \brief googletest的测试单元，用于算法函数的测试．
 *
 * \param 无
 *
 * \return 无
 *
 */
class Test_Sort : public Test
{
protected:
   // CBox* c;

    virtual void SetUp()
    {
       // c = new CBox(2, 3, 4);
    }

    void TearDown()
    {
      // delete this->c;
    }
};

TEST(my_add,case1)
{
    int a=3;
    int b=4;
    ASSERT_EQ(my_add(a,b),7);
    ASSERT_TRUE(my_add(1,0));
}


GTEST_API_ int main(int argc,char** argv)
{
    testing::InitGoogleTest(&argc, argv);
    cout<<"单元测试如下:"<<endl;
    RUN_ALL_TESTS();
    return 0;
}
