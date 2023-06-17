#ifndef UTILS_HPP
#define UTILS_HPP

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <filesystem>


namespace fg = std::filesystem;



namespace school
{
	static bool add = true;
	
	class utils
	{
		public:
			/* read file in disk and retoure in to string form 
			 * file_name : string -> file_name to read
			 */
			static std::string read_file(const std::string &file_name);


			/* write vector string into a file
			 * filename: string -> filename to write data
			 * strings: vector of string, strings to write into file
			 * mode: bool -> 'a' | 'w'
			 */
			static void write(
					const std::string& filename,
				       	const std::vector<std::string> &strings, 
					bool mode);

			/*
			 * write string into a file
			 * filename: string -> filename to write data
			 * strings: string to write into a file
			 * mode: bool -> 'true' | 'false'
			 */
			static void write(const std::string& filename, const std::string& chaines, bool mode);
	};
}

#endif
