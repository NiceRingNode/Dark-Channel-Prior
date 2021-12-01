#include "DeHazing.h"
#include "ui_DeHazing.h"

DeHazing::DeHazing(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::DeHazing)
{
    ui->setupUi(this);
}

DeHazing::~DeHazing()
{
    delete ui;
}


void DeHazing::on_use_erode_cb_toggled(bool checked)
{

}

void DeHazing::on_dark_channel_window_editingFinished()
{

}

void DeHazing::on_guided_filter_window_editingFinished()
{

}

void DeHazing::on_haze_save_ratio_editingFinished()
{

}

void DeHazing::on_threshold_t0_editingFinished()
{

}

void DeHazing::on_org_dehazed_btn_clicked()
{

}

void DeHazing::on_org_dc_btn_clicked()
{

}

void DeHazing::on_dark_channel_slider_valueChanged(int value)
{

}

void DeHazing::on_action_save_triggered()
{

}
