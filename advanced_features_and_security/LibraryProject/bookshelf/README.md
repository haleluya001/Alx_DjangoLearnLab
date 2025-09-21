Permissions and Groups Setup:

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Usage:
1. Assign users to groups via Django Admin.
2. Views are protected with @permission_required decorators.
3. Custom permissions are defined in Book.Meta.permissions.