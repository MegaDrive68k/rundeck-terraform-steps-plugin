# rundeck-terraform-steps-plugin

This is a plugin to run Terraform commands as steps in Rundeck

![dragon-ball-fusion-gohan-trunks-770x492](https://user-images.githubusercontent.com/51376003/129080403-794c3f7e-4dcd-47f8-bb2e-37fc6bf8d313.jpg)

## Prerequisites

1. Python 3.
2. Terraform binary reachable by `rundeck` user account.

## Getting the source

`git clone https://github.com/MegaDrive68k/rundeck-terraform-steps-plugin`

## Building the plugin

  1. `make clean`
  2. `make build`

## Installing the plugin on your Rundeck instance  

  1. Get the `rundeck-terraform-steps.zip` file generated at `build/libs` and copy to rundeck [libext](https://docs.rundeck.com/docs/administration/configuration/plugins/installing.html#installing-plugins) directory.

## Using the plugin

  1. Create or edit any job and you can see new node steps to add.

![Screenshot_1](https://user-images.githubusercontent.com/51376003/129086538-337288d6-7468-40bc-a2f0-7d19f4d140a2.png)

  2. Right now the available actions are: apply, get, init, plan and validate.

## Note

This is an _alpha version_, please use it before on non-prod env.
