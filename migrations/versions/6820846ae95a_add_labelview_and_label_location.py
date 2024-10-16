"""add labelview and label_location

Revision ID: 6820846ae95a
Revises: 459b653fbd86
Create Date: 2023-12-18 10:23:08.226587

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "6820846ae95a"
down_revision = "459b653fbd86"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "label_locations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("unique_id", sa.String(length=36), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_label_locations_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_label_locations")),
    )
    op.create_table(
        "label_views",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("unique_id", sa.String(length=36), nullable=False),
        sa.Column("label_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["label_id"], ["labels.id"], name=op.f("fk_label_views_label_id_labels")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_label_views")),
    )
    with op.batch_alter_table("apscheduler_jobs", schema=None) as batch_op:
        batch_op.drop_index("ix_apscheduler_jobs_next_run_time")

    op.drop_table("apscheduler_jobs")
    with op.batch_alter_table("labels", schema=None) as batch_op:
        batch_op.add_column(sa.Column("location_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f("fk_labels_location_id_label_locations"),
            "label_locations",
            ["location_id"],
            ["id"],
        )
        batch_op.drop_column("views")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("labels", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "views",
                sa.INTEGER(),
                server_default=sa.text("0"),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.drop_constraint(
            batch_op.f("fk_labels_location_id_label_locations"), type_="foreignkey"
        )
        batch_op.drop_column("location_id")

    op.create_table(
        "apscheduler_jobs",
        sa.Column("id", sa.VARCHAR(length=191), autoincrement=False, nullable=False),
        sa.Column(
            "next_run_time",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("job_state", postgresql.BYTEA(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="apscheduler_jobs_pkey"),
    )
    with op.batch_alter_table("apscheduler_jobs", schema=None) as batch_op:
        batch_op.create_index(
            "ix_apscheduler_jobs_next_run_time", ["next_run_time"], unique=False
        )

    op.drop_table("label_views")
    op.drop_table("label_locations")
    # ### end Alembic commands ###
