#include <iostream>
#include <filesystem>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include "db.hpp"

namespace fs = std::filesystem;

DB::DB(std::string db)
{
	if ( ! ( fs::exists(db ) && fs::exists( db + std::string{"/db_conf"}) ))
		std::cout << db << " non exist\n", exit(-1);

	else
	{
		db_name = db + std::string{"/db_conf"};
		data = school::utils::read_file ( db_name );
		std::cout << "succeful acce to database : " << db << "\n";
	}

}

void DB::addTable(const std::string& table_name,
				  const std::string& field)
{
	//std::string root_dir = fs::path(db).parent_path();
	std::string table = "table:"+table_name+":"+field;
	printf("add new table in to %s -> table name %s -> field %s", 
			db_name.c_str(), table_name.c_str(), field.c_str());
	school::utils::write(db_name,
						table,
						school::add);
}

DB::~DB()
{
	
}
