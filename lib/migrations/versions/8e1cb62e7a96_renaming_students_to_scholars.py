"""Renaming students to scholars

Revision ID: 8e1cb62e7a96
Revises: 791279dd0760
Create Date: 2025-03-07 14:11:56.154643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1cb62e7a96'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
