#include "../include/db.hpp"



int main(int argc, char** argv)
{
    if ( argc  < 2 )
    {
        std::cout << "argument is insuffusant\n", exit(1);
    }
	DB db { argv[1] };
    db.addTable("eleves", "str<prenom>:str<nom>:int<age>\n");
	return 0;
}

