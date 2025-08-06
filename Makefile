#------------------------------------------------------------------------------#

# List of all subderectories
SUBDIRS=`find -mindepth 1 -maxdepth 1 -type d -not -name '.*' -not -name '_*'`

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~ .*.sw?

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= ${CLEAN_FILES}

all:
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D ;            \
	done

#------------------------------------------------------------------------------#

HTML=html
PUBLISH=_publish
PROVAS=$(PUBLISH)/provas
AULAS=$(PUBLISH)/aulas

BOOK=./1-apostila/Calculo_Varias_Variaveis-1.pdf

.PHONY: publish
publish: all
	mkdir -p $(PROVAS)/2024-1
	mkdir -p $(PROVAS)/2025-1
	cp $(BOOK) $(PUBLISH)
	cp ./3-provas/2024-1/*.pdf $(PROVAS)/2024-1/
	cp ./3-provas/2025-1/*.pdf $(PROVAS)/2025-1/
	cp -r ./2-apresentacoes/pdf/2-hand $(AULAS)
	cp $(HTML)/styles.css $(PUBLISH)
	python $(HTML)/generate_index.py

#------------------------------------------------------------------------------#

.PHONY: clean
clean:
	@ rm -vf ${CLEAN_FILES}
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D clean ;      \
	done


.PHONY: distclean
distclean:
	@ rm -vf ${DISTCLEAN_FILES}
	@ for D in ${SUBDIRS}; do   \
	  make -C $$D distclean ;   \
	done
	@ rm -rf _publish

#------------------------------------------------------------------------------#
