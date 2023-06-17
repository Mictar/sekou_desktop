#include "utils.hpp"


std::string school::utils::read_file(
		const std::string &file_name)
{
	std::ifstream file {file_name};
	std::stringstream buffer;

	buffer << file.rdbuf();

	return buffer.str();
}

void school::utils::write(
		const std::string& filename, 
		const std::string& strings, 
		bool  mode=school::add)
{
	if ( mode == school::add )
	{
		std::ofstream file { filename, std::ios::app };
		file << strings;
	}
	else
	{
		std::ofstream file { filename };
		file << strings;
	}
}
void school::utils::write(
		const std::string& filename, 
		const std::vector<std::string>& strings, 
		bool  mode=school::add)
{
	std::ofstream file { filename, std::ios::app };
	std::string str;
	for ( auto itr : strings) str += itr;

	school::utils::write(filename, str, mode);
}


