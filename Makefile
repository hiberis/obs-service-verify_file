prefix = /usr

servicedir = ${prefix}/lib/obs/service

all:

install:
	install -d $(DESTDIR)$(servicedir)
	install -m 0755 verify_file $(DESTDIR)$(servicedir)
	install -m 0644 verify_file.service $(DESTDIR)$(servicedir)

.PHONY: all install
