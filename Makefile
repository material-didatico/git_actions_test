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

.PHONY: publish 
publish: all
	mkdir -p _publish/provas_anteriores
	cp ./1-apostila/Calculo_Varias_Variaveis-1.pdf _publish/
	cp -r ./2-apresentacoes/pdf/2-hand _publish/apresentacoes/
	mkdir -p _publish/provas_aneriores/2024-1
	cp ./3-provas/2024-1/*.pdf _publish/provas_aneriores/2024-1/
	mkdir -p _publish/provas_aneriores/2025-1
	cp ./3-provas/2025-1/*.pdf _publish/provas_aneriores/2025-1/

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
