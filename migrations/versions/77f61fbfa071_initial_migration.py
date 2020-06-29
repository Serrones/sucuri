"""initial migration

Revision ID: 77f61fbfa071
Revises:
Create Date: 2020-06-28 20:52:16.069439

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op


# revision identifiers, used by Alembic.
revision = "77f61fbfa071"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "label",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_label_id"), "label", ["id"], unique=False)
    op.create_table(
        "profile",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column(
            "social_media", sqlalchemy_utils.types.json.JSONType(), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_profile_id"), "profile", ["id"], unique=False)
    op.create_index(op.f("ix_profile_name"), "profile", ["name"], unique=False)
    op.create_table(
        "organization",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("about", sa.String(), nullable=True),
        sa.Column("url", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column(
            "social_media", sqlalchemy_utils.types.json.JSONType(), nullable=True
        ),
        sa.Column("owner", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["owner"], ["profile.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_organization_id"), "organization", ["id"], unique=False)
    op.create_index(
        op.f("ix_organization_name"), "organization", ["name"], unique=False
    )
    op.create_table(
        "association_org",
        sa.Column("org_id", sa.String(), nullable=True),
        sa.Column("profile_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["org_id"], ["organization.id"],),
        sa.ForeignKeyConstraint(["profile_id"], ["profile.id"],),
    )
    op.create_table(
        "project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("about", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("url", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("org", sa.String(), nullable=True),
        sa.Column(
            "social_media", sqlalchemy_utils.types.json.JSONType(), nullable=True
        ),
        sa.Column("thumbnail", sa.LargeBinary(), nullable=True),
        sa.Column(
            "media_type",
            sa.Enum("audiovisual", "blog", "podcast", "repositório", name="mediatype"),
            server_default="audiovisual",
            nullable=False,
        ),
        sa.Column(
            "course_type",
            sa.Enum("online", "presencial", name="coursetype"),
            server_default="online",
            nullable=True,
        ),
        sa.ForeignKeyConstraint(["org"], ["organization.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_project_id"), "project", ["id"], unique=False)
    op.create_index(op.f("ix_project_name"), "project", ["name"], unique=False)
    op.create_table(
        "association_label",
        sa.Column("label_id", sa.String(), nullable=True),
        sa.Column("project_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["label_id"], ["label.id"],),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"],),
    )
    op.create_table(
        "association_table",
        sa.Column("profile_id", sa.String(), nullable=True),
        sa.Column("project_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["profile_id"], ["profile.id"],),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"],),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("association_table")
    op.drop_table("association_label")
    op.drop_index(op.f("ix_project_name"), table_name="project")
    op.drop_index(op.f("ix_project_id"), table_name="project")
    op.drop_table("project")
    op.drop_table("association_org")
    op.drop_index(op.f("ix_organization_name"), table_name="organization")
    op.drop_index(op.f("ix_organization_id"), table_name="organization")
    op.drop_table("organization")
    op.drop_index(op.f("ix_profile_name"), table_name="profile")
    op.drop_index(op.f("ix_profile_id"), table_name="profile")
    op.drop_table("profile")
    op.drop_index(op.f("ix_label_id"), table_name="label")
    op.drop_table("label")
    # ### end Alembic commands ###
