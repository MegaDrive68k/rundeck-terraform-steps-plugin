all: install

clean:
	rm -rf build

build:
	mkdir -p build/libs build/zip-content/rundeck-terraform-steps
	cp -r contents resources plugin.yaml build/zip-content/rundeck-terraform-steps
	cd build/zip-content; zip -r rundeck-terraform-steps.zip *
	mv build/zip-content/rundeck-terraform-steps.zip build/libs

