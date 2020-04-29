# Documentation for Project Quay


## Contributing

Testing changes. Please ignore.

These are some really basic guidelines to get started.

Structure of this repo:
* Books go in a top level folder. For example: manage_quay.
* Each book folder has a symlink to the top level modules folder.
* A book's TOC is defined in the master.adoc file contained within the book's folder.
* master.adoc contains includes to modules (chapters) which are created in the top level modules folder.
* You will also need to define a docinfo.xml in the book's folder to contain basic information about a book.

To get started:

1. Fork this repository
2. git clone https://github.com/quay/quay-docs.git
3. cd quay-docs
4. git remote add <your-name> git@github.com:<your-name>/quay-docs.git
5. git fetch --all

To contribute:

1. git checkout master
2. git checkout -b <branch-name>
3. Edit files with changes
4. git commit -a -m "description of changes"
5. git push <your-name> <branch-name>
6. Visit https://github.com/quay/quay-docs and create pull-request against master


Once merge to master is done and you want to stage:

1. git fetch origin
2. git rebase origin/master
3. git checkout stage
4. git rebase origin/stage
5. git cherry-pick <commit-id>

In the last step, you are cherry picking the commit id of your work in the master.

More instructions to follow once we have a full fledged product.

## Deploying to OpenShift

### Adding Let's Encrypt operator in production

```bash
$ oc create -fhttps://raw.githubusercontent.com/tnozicka/openshift-acme/master/deploy/letsencrypt-live/single-namespace/{role,serviceaccount,imagestream,deployment}.yaml
$ oc policy add-role-to-user openshift-acme --role-namespace="$(oc project --short)" -z openshift-acme
```

### Deploying application template

#### Preview

```bash
$ oc new-app deployment-template.yml \
    -p NAME=projectquay-docs-preview \
    -p SOURCE_REPOSITORY_URL=https://github.com/<your-username>/quay-docs.git \
    -p SOURCE_REPOSITORY_REF=<your-current-branch>
```

#### Production

```bash
$ oc new-app deployment-template.yml \
    -p NAME=projectquay-docs-production \
    -p APPLICATION_DOMAIN=docs.projectquay.io
```
