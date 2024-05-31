## API Guide

### Base URL

The base URL for all API endpoints is `/api/committee/`.

### Endpoints

#### SocialMedia

- Endpoint: `/api/committee/socials/`
- Description: This endpoint is used to interact with the social media data of committee members.

##### CRUD Operations

1. **Create (POST)**: `/api/committee/socials/`
   - Required Parameters: `user`, `platform`, `handle`

2. **Read (GET)**: `/api/committee/socials/` and `/api/committee/socials/{id}/`
   - Required Parameters: None for `/api/committee/socials/`. For `/api/committee/socials/{id}/`, `id` is required.

3. **Update (PUT/PATCH)**: `/api/committee/socials/{id}/`
   - Required Parameters: `id`
   - Optional Parameters: `user`, `platform`, `handle`

4. **Delete (DELETE)**: `/api/committee/socials/{id}/`
   - Required Parameters: `id`

#### CommitteeMember

- Endpoint: `/api/committee/members/`
- Description: This endpoint is used to interact with the committee member data.

##### CRUD Operations

1. **Create (POST)**: `/api/committee/members/`
   - Required Parameters: `name`, `position`, `started_from`, `tenure`, `memberPhoto`, `social_media`
   - `social_media` should be a list of objects, each containing `platform` and `handle`.

2. **Read (GET)**: `/api/committee/members/` and `/api/committee/members/{id}/`
   - Required Parameters: None for `/api/committee/members/`. For `/api/committee/members/{id}/`, `id` is required.

3. **Update (PUT/PATCH)**: `/api/committee/members/{id}/`
   - Required Parameters: `id`
   - Optional Parameters: `name`, `position`, `started_from`, `tenure`, `memberPhoto`, `social_media`

4. **Delete (DELETE)**: `/api/committee/members/{id}/`
   - Required Parameters: `id`

#### CommitteeMemberCreate

- Endpoint: `/api/committee/member/create/`
- Description: This endpoint is used to create a new committee member.

##### Operations

1. **Create (POST)**: `/api/committee/member/create/`
   - Required Parameters: `name`, `position`, `started_from`, `tenure`, `memberPhoto`, `social_media`
   - `social_media` should be a list of objects, each containing `platform` and `handle`.

