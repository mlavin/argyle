Release Notes
==================

v0.2.1 (Released 2012-08-25)
--------------------------------------

- Fixed group permissions for newly created user's ssh directory


v0.2 (Released 2012-08-03)
--------------------------------------

Mostly a cleanup release. Added docs which were previously missing and a full
test suite.

Features
_________________

- Tasks for managing Node packages with npm
- Added unittest suite
- Various bug fixes/cleanup

Bug Fixes
_________________

- Fixed bug with creating a user with no groups
- Fixed bug when using upload template with a list of filenames
- Fixed incorrect error case when detecting Postgres version

Backwards Incompatible Changes
________________________________

- The default contexts for the supervisor templates have been updated slightly but were never documented


v0.1 (Released 2012-02-17)
--------------------------------------

Initial public release
