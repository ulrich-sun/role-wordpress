<<<<<<< HEAD
Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------
=======
# Automating wordpress site management actions with Ansible

Objective:

Automate primary actions on the EAZYtraining site.

Prerequisites:

- Installed on client git; zip; python3.8; wp-cli
- Installed in wp-cli wordpress container
>>>>>>> 3dfc29076d078e9d59ba9b675ade76073974716f

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

<<<<<<< HEAD
Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
=======
- Install and activate plugins and themes using wp-cli and ansibles roles
- Uninstall and deactivate plugins and themes using wp-cli and ansibles roles

### Procedure:

 1. Deploy EAZYtraining application:
	  - Git clone repos
      - Go to the directory: `cd /home/user/Role-wordpress`.
      - Type the command:
      `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags deploy`

**NB: BECOME password=${user_passord} in my case it's vagrant and Vault password=vagrant which is the password defined when creating the vault key**.

 2. Installing and activating plugins and themes

      - Go to the :

         `vi group_vars/prod.yml`

        in the form:

        `plugins_to_install:`
	   wordpress-seo`
	   malcare-security`

           To specify the list of plugins and themes to install

      - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags install_plugins`


          `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags install_themes`

      - Test the installation of plugins and themes on the customer's site:

        `wp plugin list --allow-root --ssh=docker:wordpress`
or
        `wp theme list --allow-root --ssh=docker:wordpress`


4. Get the list of installed plugins:

      - Go to the directory: `cd /home/user/Role-wordpress`.
      - Type the command:

		`ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags plugins_list`

      - Go to the ansible client and open the file: `plugins_list.json` To consult the list of installed plugins

5.  Uninstalling plugins and themes

      - Go to file :

         `vi group_vars/prod.yml `

        in the form:

        `plugins_to_uninstall:`
	  wordpress-seo`
	  `- imagify`

           To specify the list of plugins or themes to be uninstalled

      - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags uninstall_plugins`
or
          `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags uninstall_themes`


## Version 2

- Local global backup (with specific folder organization)
- Local global restore

### Execution procedure:

#### Global local backup

   Ensure that the following directories are created on the customer's premises:
         global_backup_site; global_backup_db; global_backup_plugins; global_backup_themes.

1. Local global backup (of the entire site)

      - Go to directory: `cd /home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags global_backup`

      - Go to the customer's directory: `ls /home/user/global_backup_site/`
    to view the zipped global file in this form:
    `backup_2023-11-29-150808Z_EAZYTraining_RJ80HnU9RO_global.zip`

2. Database backup

      - Go to the directory: `ls /home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags global_backup_db`

      - Go to the customer's directory: `ls /home/user/global_backup_db/`
    to view the zipped global file in this form:
    `backup_2023-11-29-150808Z_EAZYTraining_RJ80HnU9RO_global_db.sql`

3. Global backup of all plugins :

      - Go to directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags plugins_backup`


      - Go to the customer's directory: `ls /home/user/global_backup_plugins`.
    to view the zipped global file in this form:
    `backup_2023-11-29-151045Z_EAZYTraining_JJlXbmRtxY_plugins/`

4. Global backup of all themes :

      - Go to directory: `cd /home/user/Role-wordpress`
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags themes_backup`

      - Go to the customer's directory: `ls /home/user/global_backup_themes` to view the zipped global file.
    to view the zipped global file in this form:
    `backup_2023-11-29-151307Z_EAZYTraining_DivZbqEMYk_themes/`

#### Global restoration in local

   Make sure the following directories are created on the customer's site:
         global_backup_site; global_backup_db; global_backup_plugins; global_backup_themes.

1. Local global restore (of the entire site)

      - Go to :

         `vi group_vars/prod.yml`

           To specify the archived site file to be restored and the local directory where it is located (`global_backup_site` in our case):

           `backup_pattern: "backup_2023-12-11-154653Z_EAZYTraining_PppBXRbPPy_global.zip"`
           `backup_files_path: "{{ compose_project_dir }}/global_backup_site/"`

      - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags global_restore`

2. Restoring the database locally

      - Go to file :

         `vi group_vars/prod.yml`

           To specify the archived database file to be restored and the local directory where it is located (`global_backup_db` in our case):

           `restore_pattern: "backup_2023-12-08-120021Z_EAZYTraining_HNXXlsUKhE_global_db.sql"`
           `restore_files_path: "{{ compose_project_dir }}/global_backup_db"`

      - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags global_restore_db`

3. Global restoration of all plugins locally

 Go to file :

   `vi group_vars/prod.yml`

To specify the archived site file to be restored and the local directory where it is located (`global_backup_plugins` in our case):

`restore_pattern: "backup_2023-12-12-152806Z_EAZYTraining_8dd5OjIj9H_plugins.zip"
 restore_files_path: "{{ compose_project_dir }}/global_backup_plugins"`

   - Go to the directory: `/home/user/Role-wordpress`.
   - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags global_restore_plugins`.

4. Global restoration of all local themes

 Go to file :

   `vi group_vars/prod.yml`

To specify the archived site file to be restored and the local directory where it is located (`global_backup_themes` in our case):

`restore_pattern: "backup_2023-12-08-132228Z_EAZYTraining_RuOWL6ErRk_themes.zip"
 restore_files_path: "{{ compose_project_dir }}/global_backup_themes"`

   - Go to the directory: `/home/user/Role-wordpress`.
   - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags global_restore_themes`

## Version 3

- Update and Backup specific plugin and theme
- restore specific plugin (rollback)

### Execution procedure

a. Updating a specific plugin

**NB:**

**- When a specific plugin is updated, it is automatically backed up locally in the background and on the bucket.

**-At the same time, a yaml file is automatically created bearing the name of the plugin, inside which we have information on the name of the plugin, the version before the update; the name of the plugin, the version after the update and finally the date on which the plugin was updated**.

**example:**

**![](https://lh7-us.googleusercontent.com/DyCF7nxO9Go5B6jJzvnYEuoNtksRD2YQ4IlJHsgHM_ub8jop6z4KjymzIbpEusx7_AAyOkW8eC_1VnJCQE8vQiUwGCvt-SIxb5166fWKoTLMEeRrD4qE6jfOe-6pJZU63-g8o-V2rqw6LdS9mCVCsDI)**

  - Go to the file: `vi group_vars/prod.yml` and specify the plugin name and new version.
  to specify the name of the plugin to be updated and its new version

  in the form:

  `plugin_to_update:
	  plugin_name: contact-form-7
	  new_version: 5.8.4`

  - Update plugin

        - Consult the current plugin version with the command:
        `wp plugin get plugin_name --allow-root --ssh=docker:wordpress`

        - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags update_plugin`

     - Check the plugin version again with the command:

        `wp plugin get plugin_name --allow-root --ssh=docker:wordpress`

     - Go to the client file: `vi specific_backup_plugins/plugin_name.yaml` to get the update information.

     for plugin update information

     - Consult the following directory on the customer's site to view the plugin's archived file before updating: `ls specific_backup_plugins/`.


**Note: To back up and restore a specific plugin independently of its update, follow the steps below:**.

#### Specific backups

a. Local backup of a specific plugin
   - Go to the file: `vi group_vars/prod.yml`.

     in the form:

       `plugin_to_update:
	  plugin_name: contact-form-7
	  new_version: 5.8.4`

  to specify the name of the plugin to backup and its version

- Go to the directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags plugin_specific_backup`


b. Backing up the specific plugin on the s3 bucket
   - Go to the file: `vi group_vars/prod.yml` and specify the customer's directory.
  to specify the customer's directory for specific plugins to be synchronized on the bucket:
  `specific_backup_plugins: "{{ compose_project_dir }}/specific_backup_plugins/"`

- Go to the directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags s3_specific_plugins_backup

  #### Specific restore

a. Restore specific plugin locally
   - Go to file: `vi group_vars/prod.yml`.


  in the form:

  `specific_plugin_name_restore:
  restore_pattern: "backup_2023-12-22-165907Z_EAZYTraining_I6B36n43OP_contact-form-7_5.8.2.zip"
  restore_files_path: "{{ compose_project_dir }}/specific_backup_plugins"`


  to specify the name of the plugin archive to be restored and the directory where it is located.

- Go to directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags plugin_specific_restore`


b. Restoring the specific plugin from the s3 bucket
   - Download the plugin archive to be restored from the bucket:
	 - Go to the file: `vi group_vars/prod.yml` to specify the name of the archived plugin file to download:

          `s3_filename_specific_plugins: "backup_2023-12-08-134144Z_EAZYTraining_rhrwTMKhZe_updraftplus_1.23.12.zip"`

     - And the file will be stored in the `s3_specific_plugin_restore` directory on the customer's site.

- Go to directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_specific_plugins_s3`


b. Updating a specific theme

**NB:**


**- When updating a specific theme, the theme is automatically backed up locally in the background and on the bucket.


**-At the same time, a yaml file is automatically created with the theme name, containing information on the theme name, the version before the update, the theme name, the version after the update and the date on which the theme was updated**.


**example:**

**![](https://lh7-us.googleusercontent.com/MrW3vpZAGURftPtWLF_I9YpFLgK9gLrjqjZkGB79XFQdA88aL3HvGcW2nw4pKKhf4eZ9_Tv-inGRBcJz1qNUwQZiP7C7ACDsltVVznM7a5wdaJxOZWLhMh5TVqrdVdiDm6Pa5jkWNi-Z9c3P1UtgGcc)**

  - Go to file: `vi group_vars/prod.yml`

    in the form:

    `theme_to_update:
	  theme_name: "twentytwenty"
	  new_version: 1.0`

  to specify the name of the theme to be updated and its new version

  - Update theme

        - Check the current theme version with the command:
        `wp theme get nom_plugin --allow-root --ssh=docker:wordpress`

        - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags update_theme`

     - Check the plugin version again with the command:

        `wp theme get plugin_name --allow-root --ssh=docker:wordpress`

     - Go to the client file: `vi specific_backup_themes/nom_theme.yaml` to get the update information.
     for theme update information


     - Go to the following customer directory to view the theme archive before updating: `ls specific_backup_themes/`.

**Note: To backup and restore a specific theme independently of its update, follow the steps below:**.

#### Specific backups

a. Backing up a specific theme locally
   - Go to: `vi group_vars/prod.yml` file

     in the form:

    `theme_to_update:
	  theme_name: "twentytwenty
	  new_version: 1.0`

  to specify the name of the theme to backup and version

  - Go to the directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags theme_specific_backup`

b. Backing up the specific theme on the s3 bucket
   - Go to: `vi group_vars/prod.yml` file

  to specify the customer's directory for specific plugins to be synchronized on the bucket:
  `specific_backup_themes: "{{ compose_project_dir }}/specific_backup_themes/"`

- Go to the directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags s3_specific_themes_backup`

  #### Specific restore

a. Restoring the specific plugin locally
   - Go to file: `vi group_vars/prod.yml`

     in the form:

     `specific_theme_name_restore:
	  restore_pattern: "backup_2023-12-22-172456Z_EAZYTraining_vVyqa8cu45_twentytwenty_1.0.zip"
	  restore_files_path: "{{ compose_project_dir }}/specific_backup_themes

  to specify the name of the theme archive to restore and the directory where it is located.

- Go to directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags theme_specific_restore`

b. Restore specific theme from s3 bucket

   - Download the theme archive to restore from the bucket:
	 - Go to the file: `vi group_vars/prod.yml` to specify the name of the archived plugin file to download:

         `s3_filename_specific_themes: "backup_2023-12-09-171502Z_EAZYTraining_7ybgX73bqz_twentytwenty_1.1.zip"`

     - And this file will be stored in the `s3_specific_theme_restore` directory on the customer's site.

- Go to the directory: `/home/user/Role-wordpress`.
- Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_specific_themes_s3`


## Version 4

- Global backup on google drive, S3
- Global restore on google drive, S3

### Execution procedure:

#### Global Backup on bucket s3
   Make sure the following directories are created on the customer's site:
         global_backup_site; global_backup_db; global_backup_plugins; global_backup_themes.

1. Global backup on the s3 bucket (of the entire site)

      - Go to directory: `cd /home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags backup_site_s3`

      - Go to the bucket in the aws console and select the name of the bucket where the backup was made to view the zipped global file in this form:
   `backup_2023-11-29-150808Z_EAZYTraining_RJ80HnU9RO_global.zip`

2. Backing up the database on the s3 bucket

      - Go to directory: `ls /home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags backup_db_s3`

      - Go to the bucket in the aws console and choose the name of the bucket where the backup was made to view the zipped global file in this form:
    `backup_2023-11-29-150808Z_EAZYTraining_RJ80HnU9RO_global_db.sql`

3. Global backup of all plugins on bucket s3:

      - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags s3_global_plugins_backup`

      - Go to the bucket in the aws console and choose the name of the bucket where the backup was made to view the zipped global file in this form:
    `backup_2023-11-29-151045Z_EAZYTraining_JJlXbmRtxY_plugins.zip`

4. Global backup of all themes on the s3 bucket:

      - Go to directory: `cd /home/user/Role-wordpress`.
      - Type the command:
         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags s3_global_themes_backup`

      - Go to the bucket in the aws console and choose the name of the bucket where the backup was made to view the zipped global file in this form:


    `backup_2023-11-29-151307Z_EAZYTraining_DivZbqEMYk_themes.zip`

#### Global restore to s3 bucket
   Make sure that the following directories are created on the customer's site:
         s3_site_restore; s3_db_restore; s3_global_plugin_restore; s3_global_theme_restore.

1. Global restore from s3 bucket (site-wide)

    a. Download the zipped file of the site to be restored into the directory `s3_site_restore`.

      - Go to file :

         `vi group_vars/prod.yml`

           To specify the archived file for the site to be restored:

           `s3_filename_site: "backup_2023-12-11-154653Z_EAZYTraining_PppBXRbPPy_global.zip"`

      b. Restore the site by retrieving the archive from the `s3_site_restore` directory

   - Go to directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_site_s3`

2. Restoring the database from the s3 bucket

      a. Download the zipped database file to be restored into the `s3_db_restore` directory.

      - Go to file :

         `vi group_vars/prod.yml`

           To specify the site archive file to be restored:

           `s3_filename_db: "backup_2023-12-08-120021Z_EAZYTraining_HNXXlsUKhE_global_db.sql"`


      b. Restore the site by retrieving the archive from the `s3_site_restore` directory

   - Go to directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_site_s3`


2. Restoring the database from the s3 bucket

      a. Download the zipped database file to be restored into the `s3_db_restore` directory.

      - Go to file :


      b. Restore the database by retrieving the archive from the directory `s3_db_restore`.

   - Go to the directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_db_s3`

3. Global restoration of all plugins from the s3 bucket

      a. Download the zipped file of plugins to be restored into the `s3_global_plugin_restore` directory.

      - Go to file :

         `vi group_vars/prod.yml`

           To specify the site archive file to be restored:

           `s3_filename_plugins: "backup_2023-12-08-122719Z_EAZYTraining_haEVITTfu9_plugins.zip"`

      b. Restore plugins by retrieving the archive from the directory `s3_global_plugin_restore`.

   - Go to directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_plugins_s3`

4. Global restoration of all themes from the s3 bucket


      a. Download the zipped file of plugins to be restored into the `s3_global_theme_restore` directory.

      - Go to file :

         `vi group_vars/prod.yml`

           To specify the site archive file to be restored:

           `s3_filename_themes: "backup_2023-12-08-132228Z_EAZYTraining_RuOWL6ErRk_themes.zip"`

      b. Restore plugins by retrieving the archive from the `s3_global_theme_restore` directory

   - Go to directory: `/home/user/Role-wordpress`.
      - Type the command:

         `ansible-playbook -i hosts.yml --ask-vault-pass -vvv wordpress_operations.yml --tags restore_themes_s3`

## Version 5

- molecule integration
- Pre-commit hooks integration

Pre-commit hooks are an effective way to automate code verification processes and ensure the quality, security, and consistency of a software project's source code.

Here are some common security testing hooks you can use in a pre-commit pipeline:

- detect-secrets: Identifies sensitive secrets in the source code.
- detect-aws-credentials: Detects exposed AWS credentials in the code.
- detect-private-key: Searches for exposed private keys in the code.
- check-vuln-dependencies: Analyzes project dependencies for known vulnerabilities.
- dep-scan: Performs static code security analysis to identify known vulnerabilities.
- trufflehog: Searches for credentials and other secrets in the source code.
- bandit: Static analysis of Python code for security vulnerabilities.
- eslint-plugin-security: ESLint plugin that detects security vulnerabilities in JavaScript code.
- brakeman: Static security analysis tool for Ruby on Rails applications.

These hooks can be used to detect potential security issues in the source code and prevent security breaches.

**NB: In the .pre-commit-hooks.yaml file, we have implemented the detect-secrets, detect-aws-credentials, detect-private-key hooks regarding security**

1. For the detect-secrets hook, we need to ensure the following:

   - Check detect-secrets installation: Make sure you have correctly installed the detect-secrets tool in your environment. You can use the following command to install the tool:
     `python3 -m pip install detect-secrets`

   - Check execution path: Ensure that the execution path to the detect-secrets executable is included in your PATH environment variable. You can check the execution path using the following command:
     `which detect-secrets`

   - Check permissions: Ensure you have the necessary permissions to execute detect-secrets. If using sudo, make sure the execution path is correct.
     Try running the command with the full path: If you know the full path to detect-secrets, try running it directly with the full path:
     `detect-secrets scan > .secrets.baseline`

3. To execute our pre-commit hooks defined in .pre-commit-hooks.yaml follow the steps below:


    Before you can run hooks, you need to have the pre-commit package manager installed.

	Using pip:

	`pip3 install pre-commit`

	`pre-commit --version` should show you what version you're using

	- create a file named .pre-commit-config.yaml
	- you can generate a very basic configuration using pre-commit sample-config
	- the full set of options for the configuration are listed in documentation
	- other supported hooks are available in documentation
        - run `pre-commit install` to set up the git hook scripts
        - it's usually a good idea to run the hooks against all of the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks) with command: `git add .` , `pre-commit autoupdate` and `pre-commit run --all-files`
        - Then commit and push your code

## Manage user in Ansible semaphore

Ansible Semaphore is an orchestration and automation management tool that simplifies the use of Ansible by providing a graphical user interface for managing projects and tasks. When it comes to managing users and roles, Semaphore offers a flexible structure for defining who can do what within the tool. Here is an explanation of the different team-level roles and user-level permissions:

Roles at Team Level
- Owner
Permissions: Owners have full control over the team and its projects. They can manage team members, configure projects, execute and modify all tasks, and also have the rights to delete the team or modify its configurations.
- Manager
Permissions: Managers can manage project configurations within the team. They can create, modify and delete projects and tasks, but cannot modify team configurations or manage team members.
- Task Runner
Permissions: Task Runners can run tasks and view the results. They have access to projects for which they are authorised, but cannot create new projects or modify existing configurations.
- Guest
Permissions: Guests have very limited access rights, usually read-only. They can view projects and tasks, but cannot run tasks or modify anything.
User Level Permissions
- Alert
Permissions: Users with the Alert role can receive notifications about tasks or projects. This role is often used to inform stakeholders or team members who need to be kept informed of the progress or execution of tasks without being actively involved in managing them.
- Admin
Permissions: Administrators have extensive rights to Semaphore.They can manage all aspects of the application, including user, team and system configurations.They can add or remove users, manage team roles, and have access to all administrative features.

User management in Ansible Semaphore is designed to offer flexibility and granular control over who can see or do what in the tool.This structure helps secure automation environments while providing enough flexibility for different parties to collaborate effectively.Make sure you plan who needs what level of access to maintain both security and efficiency in your automation projects.

## Version 6

- galaxy role release
>>>>>>> 3dfc29076d078e9d59ba9b675ade76073974716f
