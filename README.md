# Redmineflux Workload Plugin

A Redmine plugin for team and workload management.

## Features

### Team Management
- Create, update, list, and delete teams
- Each team has a name and optional description
- Track who created each team

### Team Roles
- Define roles within teams (e.g., Manager, Lead, Member)
- Roles include `can_approve_leave` flag for future leave management
- Roles are reusable across all teams

### Team Membership
- Add users to teams with specific roles
- One role per user per team
- Prevents duplicate user entries in the same team
- Users can belong to multiple teams

## Installation

1. Copy the plugin to your Redmine `plugins` directory:
   ```bash
   cd /path/to/redmine/plugins
   git clone <repository-url> redmineflux_workload
   ```

2. Run the plugin migrations:
   ```bash
   bundle exec rake redmine:plugins:migrate RAILS_ENV=production
   ```

3. Restart Redmine

## Configuration

### Permissions

The plugin adds a global permission: **Manage teams and roles** (`manage_rf_teams`)

This permission allows users to:
- Create, edit, and delete teams
- Create team roles
- Add/remove team members
- Change member roles

To grant this permission:
1. Go to Administration → Roles and permissions
2. Select a role (e.g., Manager)
3. Enable "Manage teams and roles" permission

### Menu Access

A "Teams" menu item is automatically added to the top menu for all logged-in users.

## Usage

### Creating Team Roles

1. Navigate to Teams → Team Roles
2. Click "New Team Role"
3. Enter role name (e.g., Manager, Lead, Member)
4. Optionally check "Can approve leave" for future functionality
5. Click "Create"

### Creating Teams

1. Navigate to Teams
2. Click "New Team"
3. Enter team name and description
4. Click "Create"

### Adding Team Members

1. Open a team
2. In the "Members" section, select:
   - User from the dropdown
   - Role for that user
3. Click "Add"

### Managing Members

- View all team members in the team detail page
- Remove members using the delete icon
- Each user can only be added once per team

## Database Schema

### Tables

#### rf_teams
- `id` - Primary key
- `name` - Team name (required)
- `description` - Team description (text)
- `created_by_id` - Creator user ID
- `created_at`, `updated_at` - Timestamps

#### rf_team_roles
- `id` - Primary key
- `name` - Role name (required, unique)
- `can_approve_leave` - Boolean flag (default: false)
- `created_at`, `updated_at` - Timestamps

#### rf_team_memberships
- `id` - Primary key
- `team_id` - Foreign key to rf_teams
- `user_id` - Foreign key to users (Redmine core)
- `team_role_id` - Foreign key to rf_team_roles
- `created_at`, `updated_at` - Timestamps
- Unique constraint on [team_id, user_id]

## Technical Details

### Naming Conventions

All database tables, models, controllers, and files use the `rf_` prefix:
- Tables: `rf_teams`, `rf_team_roles`, `rf_team_memberships`
- Models: `RfTeam`, `RfTeamRole`, `RfTeamMembership`
- Controllers: `RfTeamsController`, `RfTeamRolesController`, `RfTeamMembershipsController`

### Models

- **RfTeam**: Represents a team with members
- **RfTeamRole**: Defines roles that can be assigned to team members
- **RfTeamMembership**: Join table linking teams, users, and roles

### Authorization

- Uses Redmine's built-in authorization system
- Global permission `:manage_rf_teams` required for create/update/delete operations
- Read access available to all logged-in users

## Future Enhancements

This plugin is designed to be extended with:
- Leave management functionality (using the `can_approve_leave` role flag)
- Workload tracking and allocation
- Skills management
- Availability calendars

## Development

### Code Quality

- No scaffolds or STI
- No concerns or unnecessary callbacks
- Strong parameters for security
- Follows Redmine and Rails conventions
- Clean, maintainable code structure

### Testing

Run plugin tests:
```bash
bundle exec rake redmine:plugins:test NAME=redmineflux_workload RAILS_ENV=test
```

## License

[Add your license here]

## Author

[Add author information]

## Support

For issues and feature requests, please use the issue tracker.
