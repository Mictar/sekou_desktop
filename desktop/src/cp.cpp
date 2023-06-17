#include "utils.hpp"

std::string valeur (std::string msg)
{
	if ( msg == "str" ) return "Hello";
	else if (msg == "int")
	{
		return std::to_string(2);
	}
	else return std::to_string(2.3);
	
}
int main(int argc, char** argv)
{
	auto str = school::utils::read_file(argv[1]);

	std::string cp { str };

	school::utils::write(argv[2], cp, school::add);

	return 0;
}
