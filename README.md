# rundeck-terraform-steps-plugin

This is a plugin to run Terraform commands as steps in Rundeck

![dragon-ball-fusion-gohan-trunks-770x492](https://user-images.githubusercontent.com/51376003/129080403-794c3f7e-4dcd-47f8-bb2e-37fc6bf8d313.jpg)

## Getting the source

`git clone https://github.com/MegaDrive68k/rundeck-terraform-steps-plugin`

## Building the plugin

  1. `make clean`
  2. `make build`

## Installing the plugin on your Rundeck instance  

  1. Get the `rundeck-terraform-steps.zip` file generated at `build/libs` and copy to rundeck [libext](https://docs.rundeck.com/docs/administration/configuration/plugins/installing.html#installing-plugins) directory.

## Note

This is an _alpha version_, please use it before on non-prod env.
