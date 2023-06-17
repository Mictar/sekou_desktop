
#ifndef DB_HPP
#define DB_HPP
#include "utils.hpp"

class DB : public school::utils
{
	// le conteneur du nom de la base de donnée
	std::string db_name;
	std::string data;
	public:
		DB(std::string db_name);

		/*
		 * fonction ajouter de table dans la base de donnée
		 * table_name: le nom de la table
		 * col_types: le type des column
		 * return : void
		 */
		void addTable(const std::string &table_name, const std::string & field);

		/*
		 * fonction de suppression de table dans la base de donnée
		 * table_name: le nom de la table correspondant
		 */
		bool dropTable(const std::string &table_name);

		/*
		 * fonction de renomage de d'une table par une autre
		 * old_name: l'ancien nom de la table
		 * new_name: le nouveau nom de la table
		 * return : true si tout est ok sinon false
		 */
		bool renameTable(const std::string& old_name, 
			    const std::string& new_name);

		/*
		 * fonction d'insertion des données dans une table
		 * table_name: le nom de la table
		 * data: les donnée a enregistrer
		 * return: true si tout est ok sinon false
		 */
		bool insert2Table(const std::string& table_name,
			     std::vector<std::string> data);

		/*
		 * fonction de recherche dans la base de donnée
		 * table_name: le nom de la table
		 * index: la colonne de recherche
		 * value: la valeur a recherche
		 */
		std::vector<std::string> search2Table(
			     const std::string & table_name, 
			     const std::string&  index,
			     const std::string& value);
		
		// le destructeur de la classe DB
		~DB();

};

#endif
