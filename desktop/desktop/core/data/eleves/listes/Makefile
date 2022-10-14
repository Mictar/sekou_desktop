list_rep=/home/moctar/Bureau/sekou_cisse/sekou_desktop/desktop/desktop/core/data/eleves/listes
note_rep=/home/moctar/Bureau/sekou_cisse/sekou_desktop/desktop/desktop/core/data/notes/listes
list_file=$(list_rep/*.ods)
note_rep=$(note_rep/*.ods)

note_rep: $(list_file)
	python3 $(list_rep)/lists.py