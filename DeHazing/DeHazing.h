#ifndef DEHAZING_H
#define DEHAZING_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class DeHazing; }
QT_END_NAMESPACE

class DeHazing : public QWidget
{
    Q_OBJECT

public:
    DeHazing(QWidget *parent = nullptr);
    ~DeHazing();

private slots:
    void on_use_erode_cb_toggled(bool checked);

    void on_dark_channel_window_editingFinished();

    void on_guided_filter_window_editingFinished();

    void on_haze_save_ratio_editingFinished();

    void on_threshold_t0_editingFinished();

    void on_org_dehaze_btn_clicked();

    void on_org_dc_btn_clicked();

    void on_dark_channel_slider_valueChanged(int value);

    void on_action_save_triggered();

private:
    Ui::DeHazing *ui;
};
#endif // DEHAZING_H
